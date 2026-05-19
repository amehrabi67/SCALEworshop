#include <Arduino.h>

/**
 * 1. FIX: You MUST change this name to match the EXACT .h file 
 * found in your C:\Users\Amirreza\Documents\Arduino\libraries\ project folder.
 * If this name is wrong, 'signal_t' and 'run_classifier' will fail.
 */
#include <modeh_inferencing.h> // The engine
#include "model_data.h"       // Your 7,752-byte model array

// Rest of your code...

/**
 * 2. FIX: Only include this ONCE. 
 * The guards added in Step 1 will prevent the redefinition error.
 */


// 48x48x3 image buffer
uint8_t your_image_buffer[6912]; 

/**
 * 3. Callback to provide data to the model
 */
int raw_feature_get_data(size_t offset, size_t length, float *out_ptr) {
    for (size_t i = 0; i < length; i++) {
        // Pixel scaling 0..1 based on your Edge Impulse settings
        out_ptr[i] = (float)your_image_buffer[offset + i] / 255.0f;
    }
    return 0;
}

void setup() {
    Serial.begin(115200);
    while (!Serial); 
    
    Serial.println("Renesas RA4M1 - Tiny Fruit Model Initialized");
    Serial.print("Model size: ");
    Serial.print(model_tflite_len); 
    Serial.println(" bytes.");
}

void loop() {
    // These require the <..._inferencing.h> header to be found
    signal_t features_signal;
    features_signal.total_length = EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE;
    features_signal.get_data = &raw_feature_get_data;

    ei_impulse_result_t result = { 0 };

    // Run classifier
    EI_IMPULSE_ERROR res = run_classifier(&features_signal, &result, false);

    if (res != EI_IMPULSE_OK) {
        Serial.print("ERR: Inference failed: ");
        Serial.println(res);
        return;
    }

    // Print results for your classes: "Banana 4" and "apple_braeburn_1"
    bool found = false;
    for (size_t ix = 0; ix < EI_CLASSIFIER_LABEL_COUNT; ix++) {
        if (result.classification[ix].value > 0.70) {
            Serial.print("Match: ");
            Serial.print(result.classification[ix].label); 
            Serial.print(" (");
            Serial.print(result.classification[ix].value * 100);
            Serial.println("%)");
            found = true;
        }
    }

    if (!found) { Serial.println("No fruit detected."); }

    delay(2000); 
}