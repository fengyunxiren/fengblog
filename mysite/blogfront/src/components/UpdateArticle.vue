<template>
  <div>
    <div class="header-input">
      <el-input placeholder="请输入内容" v-model="title">
        <template slot="prepend">标题</template>
      </el-input>
    </div>
    <div class="header-input">
      <el-input placeholder="请输入内容" v-model="describle">
        <template slot="prepend">简介</template>
      </el-input>
    </div>
    <mavon-editor
      v-model="content"
      ref="md"
      :defaultOpen="defaultOpen"
      :subfield="false"
      :ishljs="true"
      @save="saveArticle"
      @imgAdd="imageAdd"
      @imgDel="imageDel">
    </mavon-editor>
  </div>
</template>

<script>
export default {
  name: 'UpdateArticle',
  data () {
    return {
      msg: 'Feng\'s blog',
      defaultOpen: 'edit',
      title: '',
      describle: '',
      content: '',
      id: '',
      category: '',
      author: ''
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
            var article = JSON.parse(response.bodyText)
            this.id = article.id
            this.title = article.title
            this.describle = article.describle
            this.content = article.content
            this.category = article.category
            this.author = article.author
          } else {
            this.$message.error('get articles error!')
          }
        })
    },
    saveArticle () {
      var putData
      putData = {
        title: this.title,
        describle: this.describle,
        content: this.content,
        category: this.category,
        author: this.author
      }
      if (this.id !== '') {
        var _this = this
        this.$http.put('http://127.0.0.1:8000/api/article/' + this.id + '/', putData, {emulateJSON: true})
          .then((response) => {
            if (response.ok) {
              setTimeout(function () {
                _this.$router.push({path: '/articles/' + _this.id})
              }, 2000)
            } else {
              this.$message.error('update article failed!')
            }
          })
      } else {
        console.log(this.id)
        this.$message.error('id expect a number!')
      }
    },
    imageAdd (pos, $file) {
      var _this = this
      var formData = new FormData()
      formData.append('image', $file)
      formData.append('name', 'test')
      _this.$http.post('http://127.0.0.1:8000/api/image/', formData, {emulateJSON: true})
        .then((response) => {
          if (response.ok) {
            var data = JSON.parse(response.bodyText)
            console.log(data)
            console.log(_this.$refs)
            _this.$refs.md.$img2Url(pos, 'http://127.0.0.1:8000/' + data.image)
          } else {
            _this.$message.error('upload image error!')
          }
        })
    },
    imageDel (pos, $file) {
      console.log(pos)
    }
  }
}
</script>

<style>
  .header-input {
    margin-bottom: 5px;
  }
</style>
