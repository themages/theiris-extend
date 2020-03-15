{
    "targets": [
        {
            "target_name": "fringerprint",
            "cflags!":["-fno-exceptions"],
            "cflags_cc!": ["-fno-exceptions"],
            "sources": [
                "<!@(node -p \"require('node-addon-api').include\")"
            ],
            "defines": ["NAPI_DISABLE_CPP_EXCEPTIONS"],
        }
    ]
}