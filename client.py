class BrowserComputerUseElementAnchorClient:
    def anchor_interactive_element(self, target_intent='Click the primary Checkout button', viewport_x=740, viewport_y=512):
        return {
            'anchor_id': 'anc_claw_9102',
            'target_intent': target_intent,
            'resolved_css_selector': 'button[data-testid="checkout-submit"][aria-label="Checkout"]',
            'fallback_xpath': "//button[contains(text(), 'Checkout') or contains(@class, 'checkout-btn')]",
            'bounding_box': {'x': viewport_x, 'y': viewport_y, 'width': 220, 'height': 48},
            'confidence_score': 0.985,
            'stability_index': 'HIGH_DYNAMIC_DOM_RESILIENT',
            'telemetry_url': 'https://claw.grounding.genpark.ai/anchors/9102.json'
        }
