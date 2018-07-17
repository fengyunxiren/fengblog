<template>
  <div>
    <div v-if="defaultOpen === 'preview'">
      <div class="detail-info">
        <p class="detail-title">{{ article.title }}</p>
        <p class="detail-author">
            <span>
                <i class="el-icon-edit-outline user-editor" @click="gotoArticleUpdate()"></i>
                {{ article.nickname }}
            </span>
            <span>
                <i class="el-icon-time"></i>
                {{ article.update_time }}
            </span>
        </p>
      </div>
    </div>
    <div v-else>
      <div class="header-input">
        <el-input placeholder="请输入内容" v-model="article.title">
          <template slot="prepend">标题</template>
        </el-input>
      </div>
      <div class="header-input">
        <el-input placeholder="请输入内容" v-model="article.describle">
          <template slot="prepend">简介</template>
        </el-input>
      </div>
    </div>
    <mavon-editor id="detail-editor"
      v-model="article.content"
      ref="md"
      :defaultOpen="defaultOpen"
      :subfield="false"
      :editable="editable"
      :toolbarsFlag="toolbarsFlag"
      :ishljs="true"
      :boxShadow="false"
      @save="saveArticle"
      @imgAdd="imageAdd"
      ></mavon-editor>
  </div>
</template>

<script>
export default {
  name: 'ArticleDetail',
  data () {
    return {
      msg: 'Feng\'s blog',
      defaultOpen: 'preview',
      editable: true,
      toolbarsFlag: false,
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
    saveArticle () {
      var putData
      putData = {
        title: this.article.title,
        describle: this.article.describle,
        content: this.article.content,
        category: this.article.category,
        author: this.article.author
      }
      var _this = this
      this.$http.put('http://127.0.0.1:8000/api/article/' + _this.article.id + '/', putData, {emulateJSON: true})
        .then((response) => {
          if (response.ok) {
            this.article = JSON.parse(response.bodyText)
            this.article.update_time = this.transDate(this.article.update_time)
            this.gotoArticleDetail()
          } else {
            this.$message.error('update article failed!')
          }
        })
    },
    transDate (timeString) {
      var newString = ''
      newString = timeString.replace(/T/, ' ')
      newString = newString.split('.')[0]
      return newString
    },
    gotoArticleUpdate () {
      var _this = this
      _this.defaultOpen = 'edit'
      _this.editable = true
      _this.toolbarsFlag = true
    },
    gotoArticleDetail () {
      var _this = this
      _this.defaultOpen = 'preview'
      _this.editable = false
      _this.toolbarsFlag = false
    },
    imageAdd (pos, $file) {
      var _this = this
      var formData = new FormData()
      formData.append('image', $file)
      formData.append('name', this.article.title)
      _this.$http.post('http://127.0.0.1:8000/api/image/', formData, {emulateJSON: true})
        .then((response) => {
          if (response.ok) {
            var data = JSON.parse(response.bodyText)
            _this.$refs.md.$img2Url(pos, 'http://127.0.0.1:8000/' + data.image)
          } else {
            _this.$message.error('upload image error!')
          }
        })
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
  #detail-editor {
    min-height: 800px;
  }
  .user-editor {
    cursor: pointer;
  }
  .user-editor:hover {
    color: #85a6ff;
  }
  .header-input {
    margin-bottom: 5px;
  }
</style>
