import unittest
from unittest.mock import patch, Mock
from cliente_http import obtener_json

class TestClienteHTTP(unittest.TestCase):
    
    @patch("cliente_http.requests.get")
    def test_obtener_json_mockea_requests(self, mock_get):
        falso_resp = Mock()
        falso_resp.json.return_value = {"ok": True, "data": "test"}
        falso_resp.raise_for_status.return_value = None
        mock_get.return_value = falso_resp

        resultado = obtener_json("https://api.example.com/test")
        
        self.assertEqual(resultado, {"ok": True, "data": "test"})
        mock_get.assert_called_once_with("https://api.example.com/test", timeout=3)
    
    @patch("cliente_http.requests.get")
    def test_obtener_json_con_error_http(self, mock_get):
        falso_resp = Mock()
        falso_resp.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
        mock_get.return_value = falso_resp

        resultado = obtener_json("https://api.example.com/not-found")
        
        self.assertIsNone(resultado)
        mock_get.assert_called_once_with("https://api.example.com/not-found", timeout=3)
    
    @patch("cliente_http.requests.get")
    def test_obtener_json_con_timeout(self, mock_get):
        mock_get.side_effect = requests.exceptions.Timeout("Timeout error")
        
        resultado = obtener_json("https://api.example.com/slow")
        
        self.assertIsNone(resultado)
        mock_get.assert_called_once_with("https://api.example.com/slow", timeout=3)

if __name__ == "__main__":
    unittest.main()