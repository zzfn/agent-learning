"""
示例埋点数据
模拟电商应用的用户行为埋点
"""

# 示例埋点事件列表
SAMPLE_EVENTS = [
    {
        'event_name': 'page_view',
        'properties': {
            'page': 'product_detail',
            'product_id': 'SKU12345',
            'category': '电子产品'
        }
    },
    {
        'event_name': 'add_to_cart',
        'properties': {
            'product_id': 'SKU12345',
            'price': 299.99,
            'quantity': 1
        }
    },
    {
        'event_name': 'checkout_start',
        'properties': {
            'cart_value': 299.99,
            'item_count': 1
        }
    },
    {
        'event_name': 'payment_method_select',
        'properties': {
            'method': '支付宝'
        }
    },
    {
        'event_name': 'order_complete',
        'properties': {
            'order_id': 'ORD789456',
            'total_amount': 299.99,
            'payment_method': '支付宝'
        }
    }
]

# 用户旅程示例
USER_JOURNEY = [
    {'event_name': 'app_open', 'timestamp': '2024-01-10 10:00:00'},
    {'event_name': 'search', 'timestamp': '2024-01-10 10:00:15', 'properties': {'keyword': '手机'}},
    {'event_name': 'page_view', 'timestamp': '2024-01-10 10:00:30', 'properties': {'page': 'search_results'}},
    {'event_name': 'product_click', 'timestamp': '2024-01-10 10:01:00', 'properties': {'product_id': 'SKU12345'}},
    {'event_name': 'page_view', 'timestamp': '2024-01-10 10:01:05', 'properties': {'page': 'product_detail'}},
    {'event_name': 'add_to_cart', 'timestamp': '2024-01-10 10:02:30'},
    {'event_name': 'page_view', 'timestamp': '2024-01-10 10:02:35', 'properties': {'page': 'cart'}},
    {'event_name': 'checkout_start', 'timestamp': '2024-01-10 10:03:00'},
    {'event_name': 'page_view', 'timestamp': '2024-01-10 10:03:05', 'properties': {'page': 'checkout'}},
    {'event_name': 'payment_failed', 'timestamp': '2024-01-10 10:04:00', 'properties': {'error': 'insufficient_balance'}},
    {'event_name': 'payment_method_change', 'timestamp': '2024-01-10 10:04:30'},
    {'event_name': 'payment_success', 'timestamp': '2024-01-10 10:05:00'},
    {'event_name': 'order_complete', 'timestamp': '2024-01-10 10:05:05'},
]

# 漏斗数据示例
FUNNEL_DATA = {
    'funnel_name': '购买转化漏斗',
    'steps': [
        {
            'name': '浏览商品',
            'users': 10000,
            'conversion_rate': 100
        },
        {
            'name': '加入购物车',
            'users': 3000,
            'conversion_rate': 30
        },
        {
            'name': '进入结算',
            'users': 1500,
            'conversion_rate': 15
        },
        {
            'name': '完成支付',
            'users': 900,
            'conversion_rate': 9
        }
    ]
}

# 异常数据示例
ANOMALY_DATA = {
    'event': 'checkout_start',
    'today_count': 450,
    'yesterday_count': 1200,
    'weekly_average': 1100,
    'change_percentage': -62.5
}

# 历史基准数据
HISTORICAL_BASELINE = """
过去7天平均数据：
- checkout_start: 每日平均 1100 次
- 标准偏差: ±150 次
- 正常波动范围: 950-1250 次
"""

# 用户群体数据
COHORT_DATA = {
    '新用户': {
        'count': 1000,
        'avg_session_duration': '3.5分钟',
        'conversion_rate': '2.5%',
        'top_actions': ['浏览商品', '搜索', '加入收藏']
    },
    '活跃用户': {
        'count': 5000,
        'avg_session_duration': '12分钟',
        'conversion_rate': '8.5%',
        'top_actions': ['浏览商品', '加入购物车', '完成购买']
    },
    '流失用户': {
        'count': 3000,
        'avg_session_duration': '1.5分钟',
        'conversion_rate': '0.5%',
        'top_actions': ['打开App', '浏览首页', '退出']
    }
}

# 业务目标示例
BUSINESS_GOALS = """
1. 提升新用户 7 日留存率至 40%
2. 提高购买转化率至 12%
3. 降低购物车放弃率
4. 提升用户平均订单价值（AOV）
5. 优化支付成功率至 95% 以上
"""
