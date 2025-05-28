--- a/src/config.py
+++ b/src/config.py
@@ top
-import os
-
-# Azure Translator (TextTranslation)
-AZURE_TRANSLATOR_KEY      = "28CbNpp20JSWei…"
-AZURE_TRANSLATOR_ENDPOINT = "https://edulocal-translator.cognitiveservices.azure.com"
+# src/config.py
+import os
+
+# Azure Translator (TextTranslation)
+AZURE_TRANSLATOR_KEY      = os.getenv("AZURE_TRANSLATOR_KEY")
+AZURE_TRANSLATOR_ENDPOINT = os.getenv("AZURE_TRANSLATOR_ENDPOINT")
+REGION                    = os.getenv("REGION")
+
+# Twilio WhatsApp Sandbox
+TWILIO_ACCOUNT_SID     = os.getenv("TWILIO_ACCOUNT_SID")
+TWILIO_AUTH_TOKEN      = os.getenv("TWILIO_AUTH_TOKEN")
+TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")
