# pattern-recognition-project-2022-2023
## [Universirty of Piraeus](https://www.unipi.gr/unipi/en/)<br>[Department of Informatics](https://www.cs.unipi.gr/index.php?lang=en)
### Course: Pattern Recognition
### Semester: 5
### Project Completion Year: 2023
### Project Team: [Dimitris Stylianou](https://github.com/dimitrisstyl7) | [Panagiota Nicolaou](https://github.com/panagiota02) | [Anastasios Baikas](https://github.com/TasosBaikas)

---

### def load_data<br>
The load_data() function reads the data from a CSV file and returns a pandas DataFrame. The file path used in the function is an absolute path, which means that it specifies the exact location of the file on your computer. If you want to use a relative path, which is a path relative to the location of the Python script, you can change the file path to 'housing.csv' as shown in the commented line of code.

### def normalize_data<br>
  The normalize_data function is using the MinMaxScaler from scikit-learn to scale the input data to the range [0, 1000]. The transformed data will have the same shape as the input data.

### def plot_pdf_histograms<br>
  The plot_pdf_histograms() function takes in two arguments:<br>
  **data_for_pdf_plot:** This is a NumPy array that contains the data to be plotted. Each column represents a variable and each row represents an observation.<br>**data_columns_names:** This is a list that contains the names of the variables in the data_for_pdf_plot array.

  The function loops through each column in the data_for_pdf_plot array and calculates the PDF (probability density function) using the norm.pdf() function from the scipy.stats module. It then plots a histogram of the data using the hist() function from Matplotlib and overlays the PDF on top of the histogram using the plot() function from Matplotlib. The function also sets the title of the plot to the name of the variable using the title() function from Matplotlib.

### def _2d_scatter_plot_with_2_attributes<br>
This function takes in two lists, data_columns_names and data_columns_values, which represent the names and values of two attributes of a dataset, and plots a 2D scatter plot with the two attributes on the x and y axes, respectively.

### def _2d_scatter_plot_with_3_attributes<br>
This function is similar to the previous one, but takes in three lists instead of two, with the third list representing a third attribute of the dataset that is used to color the markers on the scatter plot.

### def _2d_scatter_plot_with_4_attributes<br>
This function is similar to the previous one, but takes in four lists instead of three, with the fourth list representing a fourth attribute of the dataset that is used to vary the size of the markers on the scatter plot.
