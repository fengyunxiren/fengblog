<template>
    <el-card class="box-card">
      <div v-for="article in articles" :key="article.id" class="article">
        <div class="info">
            <p class="title" @click="getArticleDetail(article.id)">{{ article.title }}</p>
            <p class="author">
                <span>
                    <i class="el-icon-edit-outline"></i>
                    {{ getAuthor(article.author) }}
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
<!--         <div class="likes">
            <el-row type="flex" class="home-row-bg">
              <el-col :span="16" class="home-row-bg"><div class="home-grid-content">
                <el-tag
                  v-for="tag in article.tags"
                  :key="tag.id"
                  size="mini">
                  {{tag.name}}
                </el-tag>
              </div></el-col>
              <el-col :span="8" class="home-row-bg"><div class="home-grid-content">
                <p class="home-likes">
                    <span class="home-likes-reader">
                        <i class="el-icon-view"></i>
                        {{ article.likes.readers }}
                    </span>
                    <span class="home-likes-like">
                        <i class="el-icon-star-on"></i>
                        {{ article.likes.like.length }}
                    </span>
                    <span class="home-likes-disagree">
                        <i class="el-icon-caret-bottom"></i>
                        {{ article.likes.disagree.length }}
                    </span>
                    <span>
                        <i class="el-icon-message"></i>
                    </span>
                </p>
              </div></el-col>
            </el-row>
        </div> -->
      </div>
    </el-card>
</template>

<script>
export default {
  name: 'Main',
  data () {
    return {
      msg: 'this is main',
      articles: []
    }
  },
  mounted: function () {
    this.showArticles()
  },
  methods: {
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
    getAuthor (id) {
      this.$http.get('http://127.0.0.1:8000/api/author/' + id.toString() + '/?format=json')
        .then((response) => {
          if (response.ok) {
            var data = JSON.parse(response.bodyText)
            console.log(data)
            this.author = data.nickname
          } else {
            this.author = 'unknown'
          }
        })
      return this.author
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
    }
  }
}
</script>

<style>
  .box-card {
    width: 80%;
    height: auto;
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
</style>
