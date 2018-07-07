<template>
  <div>
    <div class="detail-info">
      <p class="detail-title">{{ article.title }}</p>
      <p class="detail-author">
          <span>
              <i class="el-icon-edit-outline user-editor" @click="gotoArticleUpdate(article.id)"></i>
              {{ article.nickname }}
          </span>
          <span>
              <i class="el-icon-time"></i>
              {{ article.update_time }}
          </span>
      </p>
    </div>
    <mavon-editor class="detail-editor"
      v-model="article.content"
      defaultOpen="preview"
      :subfield="false"
      :editable="false"
      :toolbarsFlag="false"
      :ishljs="true"
      :boxShadow="false"
      ></mavon-editor>
  </div>
</template>

<script>
export default {
  name: 'ArticleDetail',
  data () {
    return {
      msg: 'Feng\'s blog',
      article: {}
    }
  },
  mounted: function () {
    this.showArticles()
  },
  methods: {
    showArticles () {
      var id = ''
      id = this.$route.params.id
      this.$http.get('http://127.0.0.1:8000/api/article/' + id + '/')
        .then((response) => {
          if (response.ok) {
            this.article = JSON.parse(response.bodyText)
            this.article.update_time = this.transDate(this.article.update_time)
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
    gotoArticleUpdate (id) {
      var _this = this
      _this.id = id
      setTimeout(function () {
        _this.$router.push({path: '/article/update/' + _this.id})
      }, 2000)
    }
  }
}
</script>

<style>
  .detail-info {
    background-color: #fff;
  }
  .detail-title {
    margin-top: 20px;
    margin-bottom: 0px;
    color: #000;
    font-weight: 600;
    font-size: 60px;
    cursor: pointer;
  }
  .detail-author {
    margin-top: 15px;
    margin-bottom: 0px;
    font-size: 12px;
    color: #372d30;
    text-align: left;
    text-indent: 6px;
  }
  .detail-editor {
    border-left-color: #fff;
  }
  .user-editor {
    cursor: pointer;
  }
  .user-editor:hover {
    color: #85a6ff;
  }
</style>
