import Vue from "vue";

// Function to add or update query parameters in a simplified format
const generateFilterParam = (currentParams, newParams) => {
  const updatedFilters = {
    ...currentParams,
  };

  if (currentParams.hasOwnProperty("filters")) {
    var dm = currentParams.filters;

    const splitByPipe = decodeURIComponent(dm).split("|");
    // Split each part by colon ":" and convert to key-value pairs
    let keyValuePairs = splitByPipe.reduce((result, part) => {
      const [key, value] = part.split(":");
      result[key] = value;
      return result;
    }, {});

    // Loop through keys in newParams
    for (const key in newParams) {
      if (keyValuePairs.hasOwnProperty(key)) {
        // Check if the value in newParams is not null
        if (
          newParams[key] !== null &&
          newParams[key] !== "" &&
          newParams[key] !== "" &&
          newParams[key] !== undefined
        ) {
          keyValuePairs[key] = newParams[key];
        } else {
          delete keyValuePairs[key];
        }
      } else {
        keyValuePairs[key] = newParams[key];
      }
    }

    delete updatedFilters["filters"];

    keyValuePairs = Object.fromEntries(
      Object.entries(keyValuePairs).filter(
        ([key, value]) => value !== "" && value !== undefined
      )
    );

    const urlEncodedString = Object.entries(keyValuePairs)
      .map(([key, value]) => `${key}%3A${encodeURIComponent(value)}`)
      .join("|");

    if (Object.keys(urlEncodedString).length !== 0) {
      updatedFilters["filters"] = urlEncodedString;
    }
  } else {
    const urlEncodedString = Object.entries(newParams)
      .map(([key, value]) => `${key}%3A${encodeURIComponent(value)}`)
      .join("|");
    updatedFilters["filters"] = urlEncodedString;
  }

  return updatedFilters;
};

const getFilterParams = (currentParams, params) => {
  const resultObject = {};
  params.forEach((key) => {
    resultObject[key] = null;
  });

  if (currentParams.hasOwnProperty("filters")) {
    var dm = currentParams.filters;

    const splitByPipe = decodeURIComponent(dm).split("|");
    // Split each part by colon ":" and convert to key-value pairs
    const keyValuePairs = splitByPipe.reduce((result, part) => {
      const [key, value] = part.split(":");
      result[key] = value;
      return result;
    }, {});

    for (const key in resultObject) {
      if (keyValuePairs.hasOwnProperty(key)) {
        resultObject[key] = keyValuePairs[key];
      }
    }
  }
  return resultObject;
};

Vue.prototype.$generateFilterParam = generateFilterParam;
Vue.prototype.$getFilterParams = getFilterParams;
