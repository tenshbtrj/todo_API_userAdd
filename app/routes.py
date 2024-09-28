from flask import jsonify

def register_routes(app):
    @app.route('/api', methods=['GET'])
    def get_data():
        return jsonify({'message': 'Hello, World!'})

    @app.route('/api', methods=['POST'])
    def post_data():
        # リクエストからデータを取得
        return jsonify({'received': 'データ'})  # 必要な処理を実装
