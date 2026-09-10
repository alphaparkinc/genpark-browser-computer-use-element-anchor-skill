from client import BrowserComputerUseElementAnchorClient

def main():
    client = BrowserComputerUseElementAnchorClient()
    res = client.anchor_interactive_element()
    print('Browser Element Anchor: ' + res['anchor_id'] + ' (' + res['target_intent'] + ')')
    print('Selector: ' + res['resolved_css_selector'] + ' | Confidence: ' + str(res['confidence_score']))
    print('Stability: ' + res['stability_index'] + ' | Telemetry: ' + res['telemetry_url'])

if __name__ == '__main__':
    main()
