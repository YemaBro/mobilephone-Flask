from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_args
import config


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mobilephone'
mongo = PyMongo(app)
app.config.from_object(config)


@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('cnmo'))


@app.route('/mobilephone/cnmonews/', defaults={'page': 1}, methods=['GET'])
@app.route('/mobilephone/cnmonews', defaults={'page': 1}, methods=['GET'])
@app.route('/mobilephone/cnmonews/<int:page>', methods=['GET'])
@app.route('/mobilephone/cnmonews/<int:page>/', methods=['GET'])
def cnmo(page):
    if request.method == 'GET':
        total = mongo.db.CnmoNews.count_documents({})
        page, per_page, offset = get_page_args(page_parameter='page',
                                               per_page_parameter='per_page')
        cnmonews = mongo.db.CnmoNews.find({}, {'_id': 0}).sort([('date', -1)]).limit(10).skip(10*(page-1))
        pagination = Pagination(page=page,
                                total=total,
                                record_name='cnmonnews',
                                format_number=True,
                                format_total=True,
                                css_framework='foundation')
        return render_template('cnmo.html',
                               cnmonews=cnmonews,
                               pagination=pagination,
                               per_page=per_page)
    else:
        return 'Request Error'


@app.route('/mobilephone/pconlinenews/', defaults={'page': 1}, methods=['GET'])
@app.route('/mobilephone/pconlinenews', defaults={'page': 1}, methods=['GET'])
@app.route('/mobilephone/pconlinenews/<int:page>', methods=['GET'])
@app.route('/mobilephone/pconlinenews/<int:page>/', methods=['GET'])
def pconline(page):
    if request.method == 'GET':
        total = mongo.db.PconlineNews.count_documents({})
        page, per_page, offset = get_page_args(page_parameter='page',
                                               per_page_parameter='per_page')
        pconlinenews = mongo.db.PconlineNews.find({}, {'_id': 0}).sort([('date', -1)]).limit(10).skip(10*(page-1))
        pagination = Pagination(page=page,
                                total=total,
                                record_name='pconlinenews',
                                format_number=True,
                                format_total=True,
                                css_framework='foundation')
        return render_template('pconline.html',
                               pconlinenews=pconlinenews,
                               pagination=pagination,
                               per_page=per_page)
    else:
        return 'Request Error'


@app.route('/mobilephone/zolnews/', defaults={'page': 1}, methods=['GET'])
@app.route('/mobilephone/zolnews', defaults={'page': 1}, methods=['GET'])
@app.route('/mobilephone/zolnews/<int:page>', methods=['GET'])
@app.route('/mobilephone/zolnews/<int:page>/', methods=['GET'])
def zol(page):
    if request.method == 'GET':
        total = mongo.db.ZolNews.count_documents({})
        page, per_page, offset = get_page_args(page_parameter='page',
                                               per_page_parameter='per_page')
        zolnews = mongo.db.ZolNews.find({}, {'_id': 0}).sort([('date', -1)]).limit(10).skip(10*(page-1))
        pagination = Pagination(page=page,
                                total=total,
                                record_name='zolnews',
                                format_number=True,
                                format_total=True,
                                css_framework='foundation')
        return render_template('zol.html',
                               zolnews=zolnews,
                               pagination=pagination,
                               per_page=per_page)
    else:
        return 'Request Error'


@app.route('/search/')
def search():
    q = request.args.get('q')
    total = mongo.db.CnmoNews.find({'$or': [{'title': {'$regex': q}}]}).count()
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    s_cnmonews = mongo.db.CnmoNews.find({'$or': [{'title': {'$regex': q}}]}, {'_id': 0}).sort([('date', -1)]).limit(10).skip(10*(page-1))
    pagination = Pagination(page=page,
                            total=total,
                            record_name='s_cnmonews',
                            format_number=True,
                            format_total=True,
                            css_framework='foundation')
    return render_template('search.html',
                           s_cnmonews=s_cnmonews,
                           pagination=pagination,
                           per_page=per_page)


if __name__ == '__main__':
    app.run(debug=True)
