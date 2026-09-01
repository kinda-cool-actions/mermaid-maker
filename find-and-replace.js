
export default{
  find: /@v\d+\.\d+\.\d+/g,
  replace: `@${process.env.RELEASE_TAG}`,
  files: ['README.md']
}