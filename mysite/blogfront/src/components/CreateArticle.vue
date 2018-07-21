<template>
    <div>
      <div class="header-input">
        <el-row class="demo-autocomplete">
          <el-col :span="20">
            <el-input placeholder="请输入内容" v-model="title" maxlength="80px">
              <template slot="prepend">标题</template>
            </el-input>
          </el-col>
          <el-col :span="4" class="header-col">
            <el-select v-model="categoryId" placeholder="请选择主题">
              <el-option
                v-for="category in categorys"
                :key="category.id"
                :label="category.name"
                :value="category.id">
              </el-option>
            </el-select>
          </el-col>
        </el-row>
      </div>
      <div class="header-input">
        <el-input placeholder="请输入内容" v-model="describle">
          <template slot="prepend">简介</template>
        </el-input>
      </div>
      <mavon-editor id="creater-editor"
        v-model="content"
        ref="md"
        :defaultOpen="defaultOpen"
        :subfield="false"
        :ishljs="true"
        :boxShadow="false"
        @save="saveArticle"
        @imgAdd="imageAdd">
      </mavon-editor>
    </div>
</template>

<script>
export default {
  name: 'CreateArticle',
  data () {
    return {
      message: 'this is create page',
      defaultOpen: 'edit',
      title: '',
      describle: '',
      content: '',
      categoryId: '',
      author: 1,
      categorys: {}
    }
  },
  mounted: function () {
    this.getCategorys()
  },
  methods: {
    getCategorys () {
      this.$http.get('/api/category/?format=json')
        .then((response) => {
          if (response.ok) {
            this.categorys = JSON.parse(response.bodyText)
          } else {
            this.$message.error('get categorys error!')
          }
        })
    },
    saveArticle () {
      if (this.title === '' || this.author === '' || this.categoryId === '' || this.content === '') {
        this.$message.error('title and category and conten is expected!')
        return
      }
      var describle
      if (this.describle === '') {
        if (this.content.length < 250) {
          describle = this.content
        } else {
          describle = this.content.slice(0, 250)
          describle += '...'
        }
      } else {
        describle = this.describle
      }
      var postData
      postData = {
        title: this.title,
        describle: describle,
        content: this.content,
        category: this.categoryId,
        author: this.author
      }
      var _this = this
      _this.$http.post('/api/article/', postData, {emulateJSON: true})
        .then((response) => {
          if (response.ok) {
            var article = JSON.parse(response.bodyText)
            setTimeout(function () {
              console.log(_this.id)
              _this.$router.push({path: '/articles/' + article.id})
            }, 2000)
          } else {
            this.$message.error('update article failed!')
          }
        })
    },
    imageAdd (pos, $file) {
      var _this = this
      var formData = new FormData()
      formData.append('image', $file)
      if (this.title === '') {
        formData.append('name', this.title)
      } else {
        formData.append('name', 'unknown')
      }

      _this.$http.post('/api/image/', formData, {emulateJSON: true})
        .then((response) => {
          if (response.ok) {
            var data = JSON.parse(response.bodyText)
            _this.$refs.md.$img2Url(pos, '/' + data.image)
          } else {
            _this.$message.error('upload image error!')
          }
        })
    }
  }
}
</script>
<style>
  .header-col {
    background-color: #FFF;
  }
  .header-item {
    text-align: right;
    float: right;
  }
  #creater-editor {
    min-height: 800px;
  }
</style>
