{% extends 'admin/base.html' %}
{% block content %}
<h2>Admin Dashboard</h2>
<div class="row">
    <div class="col-md-4">
        <div class="card p-3">Total Orders: {{ orders }}</div>
    </div>
    <div class="col-md-4">
        <div class="card p-3">Total Products: {{ products }}</div>
    </div>
    <div class="col-md-4">
        <div class="card p-3">Total Workers: {{ workers }}</div>
    </div>
</div>
{% endblock %}
