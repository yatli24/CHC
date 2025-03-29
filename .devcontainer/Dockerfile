FROM python:3.11

# Set the working directory
WORKDIR /workspace

# Install necessary packages
RUN pip install --no-cache-dir jupyter pandas numpy xarray

# Expose Jupyter Notebook port
EXPOSE 8888

# Command to run Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]