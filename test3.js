var schema = {
    "id": "/SimplePerson",
    "type": "object",
    "properties": {
      "name": {"type": "string"},
      "address": {
    "id": "/SimpleAddress",
    "type": "object",
    "properties": {
      "lines": {
        "type": "array",
        "items": {"type": "string"}
      },
      "zip": {"type": "string"},
      "city": {"type": "string"},
      "country": {"type": "string"}
    },
    "required": ["country"]
       },
      "votes": {"type": "integer", "minimum": 1}
    }
  };
  
  var p = {
    "name": "Barack Obama",
    "address": {
      "lines": [ "1600 Pennsylvania Avenue Northwest" ],
      "zip": 340000,
      "city": "Washington",
      "country": "USA"
    },
    "votes": 100
  };
  
  const validateObject = (schema, data) => {
    let validatedErrors = {valid: true, errors: []}
    validateObjHelper(validatedErrors, schema, data, null);
    return validatedErrors
  }
  
  const validateObjHelper = (validatedErrors, schema, data, prevKey) => {
      if (!schema.properties){
        return validatedErrors
      }
      const ppt = schema.properties
      for(var key in ppt) {
        let error = "";
        if(prevKey) {
          error = validateField(ppt[key], data[prevKey][key], key);
        }
        else {
          error = validateField(ppt[key], data[key], key);
        }
        if (error.length > 0){
          // ["dnkn"] merge ["djdd", ["dldkdkd"]]
          _merge(validatedErrors.errors, error);
          // validatedErrors.errors.extend(error);
        }
        if (ppt[key].properties){
          const err = validateObjHelper(validatedErrors, ppt[key], data, key);
        }
      }
    
      if (validatedErrors.errors){
        validatedErrors.valid = false;
      }
      return validatedErrors
    
  }
  
  const validateField = (schemaRules, data, objKey) => {
    // {"type": "string"},  "Barack Obama"
    let errors = []
    for (var key in schemaRules){
      let error = "";
      switch(key){
        case "type":
          error = validateType(schemaRules[key], data, objKey)
          break
        case "minimum":
          error = validateMin(schemaRules[key], data, objKey)
          break
        case "maximum":
          error = validateMax(schemaRules[key], data, objKey)
          break
        default:
          break;
      }
      if (error){
        errors.push(error)
      }
    }
    return errors
  }

  
  const validateType = (type, data, key) => {
      switch (type) {
          case "string":
              if(typeof data != "string"){
                  return `${key}: received ${typeof data} instead of type ${type}`    
              }
              break;
          case "integer":
              if(typeof data != "number"){
                  return `${key}: received ${typeof data} instead of type ${type}`
              }
              break
          case "array":
              if(!Array.isArray(data)){
                  return `${key}: received ${typeof data} instead of type ${type}`
              }
            break
          case "object":
            if(!_isObject(data)){
                return `${key}: received ${typeof data} instead of type ${type}`
            }
  
          default:
              break;
      }
      return ""
    }
  
    const validateMin = (min, data, key) => {
        if(typeof data == "string"){
          const len = data.length;
          if (len < min){
            return `${key}: received length of ${len}, min length is ${min}`
          }
        }else {
          if (data < min){
            return `${key}: received ${data}, min length is ${min}`
          }
        }
        return ""
      }
      
    const validateMax = (max, data) => {
        if(typeof data == "string"){
          const len = data.length;
          if (len > max){
            return `${key}: received length of ${len}, max length is ${max}`
          }
        }else {
          if (data > max){
            return `${key}: received ${data}, max length is ${max}`
          }
        }
        return ""
    }
  
  const _merge = (parent, child) => {
    for (val in child){
      parent.push(child[val])
    }
  }

  const _isObject = (obj) => {
    return obj === Object(obj);
  }
  
  console.log(validateObject(schema, p))
  
  
  
  
  
  



















//   const validateType = (type, data, key) => {
//     switch (type) {
//         case "string":
//             if(typeof data != "string"){
//                 return `${key}: received ${typeof data} instead of type ${type}`
//             }
//             break;
//         case "integer":
//             if(typeof data != "number"){
//                 return `${key}: received ${typeof data} instead of type ${type}`
//             }
//             break;
//         case "array":
//             if(!Array.isArray(data)){
//                 return `${key}: received ${typeof data} instead of type ${type}`
//             }
//             break;
//         case "object":
//             if(!_isObject(data)){
//                 return `${key}: received ${typeof data} instead of type ${type}`
//             }
//             break;

//         default:
//             break;
//     }
//     return ""
//   }




// const validateType = (type, data, key) => {
//     if(typeof data !== type){
//       if (typeof data === "number" && type == "integer"){
//         return ""
//       }
//       return `${key}: received ${typeof data} instead of type` 
//     }
//     return ""
// }


  