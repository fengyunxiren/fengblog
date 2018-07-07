<template>
  <div>
    <el-card class="box-card">
      <div v-for="article in articles" :key="article.id" class="article">
        <div class="info">
            <p class="title" @click="getArticleDetail(article.id)">{{ article.title }}</p>
            <p class="author">
                <span>
                    <i class="el-icon-edit-outline"></i>
                    {{ article.nickname }}
                </span>
                <span>
                    <i class="el-icon-time"></i>
                    {{ transDate(article.update_time) }}
                </span>
            </p>
        </div>
        <div class="abstract">
            <p class="abstract-info">
                {{ article.describle }}
            </p>
        </div>
      </div>
    </el-card>
    <el-card class="aside-card">
      <div class="category-title">
        <p>主题:</p>
      </div>
      <div class="category-all" @click="showArticles()">
        全部
      </div>
      <div class="category" v-for="category in categorys" :key="category.name" @click="selectCategory(category.name)">
          {{ category.name }}
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'Main',
  data () {
    return {
      msg: 'this is main',
      articles: [],
      categorys: []
    }
  },
  mounted: function () {
    this.init()
  },
  methods: {
    init () {
      this.showArticles()
      this.showCategorys()
    },
    showArticles () {
      this.$http.get('http://127.0.0.1:8000/api/article/?format=json')
        .then((response) => {
          if (response.ok) {
            this.articles = JSON.parse(response.bodyText)
          } else {
            this.$message.error('get articles error!')
          }
        })
    },
    transDate (timeString) {
      var newString = ''
      newString = timeString.replace(/T/, ' ')
      newString = newString.split('.')[0]
      return newString
    },
    getArticleDetail (id) {
      var _this = this
      _this.id = id
      setTimeout(function () {
        console.log(_this.id)
        _this.$router.push({path: '/articles/' + _this.id})
      }, 2000)
    },
    showCategorys () {
      this.$http.get('http://127.0.0.1:8000/api/category/?format=json')
        .then((response) => {
          if (response.ok) {
            this.categorys = JSON.parse(response.bodyText)
          } else {
            this.$message.error('get categorys error!')
          }
        })
    },
    selectCategory (name) {
      this.$http.get('http://127.0.0.1:8000/api/article/?format=json')
        .then((response) => {
          if (response.ok) {
            var data = JSON.parse(response.bodyText)
            var tmp = []
            for (var j = 0; j < data.length; j++) {
              if (data[j].category_name === name) {
                tmp.push(data[j])
              }
            }
            this.articles = tmp
          } else {
            this.$message.error('get articles error!')
          }
        })
    }
  }
}
</script>

<style>
  .box-card {
    width: 80%;
    height: auto;
    float: left;
    min-height: 1080px;
  }
  .category-title {
    text-align: left;
    color: #909399;
  }
  .category-all{
    text-align: left;
    margin-top: 10px;
    margin-bottom: 5px;
    border: 1px solid #ea6f6f;
    border-radius: 15px;
    padding-top: 4px;
    padding-bottom: 4px;
    padding-left: 15px;
    background-color: #FFF;
    color: #ea6f6f;
    font-size: 15px;
    cursor: pointer;
    min-height: 20px;
  }
  .category-all:hover {
    background-color: #FFF;
    border-color: #85a6ff;
    color: #85a6ff;
  }
  .category{
    text-align: left;
    margin-top: 10px;
    margin-bottom: 5px;
    border: 1px solid #ea6f6f;
    border-radius: 15px;
    padding-top: 4px;
    padding-bottom: 4px;
    padding-left: 15px;
    background-color: #ea6f6f;
    color: #fff;
    font-size: 15px;
    cursor: pointer;
    min-height: 20px;
  }
  .category:hover {
    background-color: #FFF;
    border-color: #85a6ff;
    color: #85a6ff;
  }
  .article {
    text-align: left;
    line-height: 1px;
    min-height: 100px;
    border-top-style: solid;
    border-color: #E1E1E1;
    border-width: 0.1em;
    background-color: f4f4f4;
  }
  .info {
    min-height: 35px;
  }
  .title {
    margin-top: 20px;
    margin-bottom: 0px;
    color: #ea6f6f;
    font-weight: 500;
    font-size: 20px;
    cursor: pointer;
  }
  .title:hover {
    color: #85a6ff;
  }
  .author {
    margin-top: 15px;
    margin-bottom: 0px;
    font-size: 12px;
    color: #372d30;
    text-indent: 6px;
  }
  .abstract {
    font-size: 15px;
    margin-top: 10px;
    margin-bottom: 0px;
    line-height: 20px;
  }
  .home-row-bg {
    max-height: 35px;
    vertical-align: middle;
  }
  .home-likes {
    vertical-align: middle;
    text-align: right;
    margin: 0px;
  }
  .home-likes-reader {
    color: #000;
  }
  .home-likes-like {
    color: #ea6f6f;
  }
  .home-likes-disagree {
    color: #c3c7b9;
  }
  .aside-card {
    width: 19%;
    height: auto;
    float: right;
    min-height: 1080px;
    background-color: f4f4f4;
  }
</style>
