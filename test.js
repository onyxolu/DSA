

// https://dev.to/franciscomendes10866/schema-validation-with-joi-and-node-js-1lma
// const scheme = Joi.object({
//     title: Joi.string().min(3).max(30).required(),
//     content: Joi.string().min(24).max(200).required()
// })

const schema = {
    title: {
        type: "string",
        minMaxLength: [3,30],
        required: true
    },
    content: {
        type: "string",
        minMaxLength: [100,300],
        required: true
    },
}

const data = {
    title: "this is my title",
    content: "this is the content and should be a bit long"
}

// string, number, required, array, regex

const validator = (schema, data) => {
    let validatorErrors = {error: {}};
    if (schema.length !== data.length){
        return Error("schema and data length mismatch");
    }
    for (var key in schema) {
        const error = validateField(schema[key], data[key])
        if (error.length > 0){
            validatorErrors.error[key] = error;
        }
    }
    return validatorErrors
}

const validateField = (schemaRules, data) => {
    errors = []
    for (var key in schemaRules) {
        let error = ""
        switch (key) {
            case "type":
                error = validateType(schemaRules[key], data);
                if (error) errors.push(error);
                break;
            case "minMaxLength":
                error = validateMinMaxLength(schemaRules[key], data);
                if (error) errors.push(error);
                break;
            case "required":
                error = validateRequired(schemaRules[key], data);
                if (error) errors.push(error);
                break;
        
            default:
                break;
        }
    }
    return errors
}

// validate helpers

const validateType = (type, data) => {
    if (typeof data !== type){
        return `expected ${type} and got ${typeof data} instead`
    }
    else return ""
}

const validateMinMaxLength = ([min, max], data) => {
    const len = data.length;
    if (len >= min && len <= max){
        return ""
    }
    else return `length of field does not meet requirement min:${min} and max:${max}`
}

const validateRequired = (required, data) => {
    if (required) {
        if (data.length > 0){
            return ""
        }
    }
    return "field is required"
}




console.log(validator(schema, data));