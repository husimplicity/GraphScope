/*
 * Copyright 2022 Alibaba Group Holding Limited.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *  	http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */

package com.alibaba.graphscope.example.giraph.format;

import com.alibaba.graphscope.example.giraph.writable.MultipleLongWritable;
import com.google.common.collect.Lists;

import org.apache.giraph.edge.Edge;
import org.apache.giraph.io.formats.TextVertexInputFormat;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.InputSplit;
import org.apache.hadoop.mapreduce.TaskAttemptContext;

import java.io.IOException;
import java.util.List;

public class P2PVertexMultipleLongInputFormat
        extends TextVertexInputFormat<LongWritable, MultipleLongWritable, MultipleLongWritable> {

    /**
     * The factory method which produces the {@link TextVertexReader} used by this input format.
     *
     * @param split   the split to be read
     * @param context the information about the task
     * @return the text vertex reader to be used
     */
    @Override
    public TextVertexInputFormat<LongWritable, MultipleLongWritable, MultipleLongWritable>
                    .TextVertexReader
            createVertexReader(InputSplit split, TaskAttemptContext context) throws IOException {
        return new P2PVertexReader();
    }

    public class P2PVertexReader extends TextVertexReaderFromEachLineProcessed<String[]> {

        String SEPARATOR = " ";

        /**
         * Cached vertex id for the current line
         */
        private LongWritable id;

        private MultipleLongWritable value;

        @Override
        protected String[] preprocessLine(Text line) throws IOException {
            //            logger.debug("line: " + line.toString());
            String[] tokens = line.toString().split(SEPARATOR);
            //            logger.debug(String.join(",", tokens));
            id = new LongWritable(Long.parseLong(tokens[0]));
            value = new MultipleLongWritable(Long.parseLong(tokens[1]));
            return tokens;
        }

        @Override
        protected LongWritable getId(String[] tokens) throws IOException {
            return id;
        }

        @Override
        protected MultipleLongWritable getValue(String[] tokens) throws IOException {
            return value;
        }

        @Override
        protected Iterable<Edge<LongWritable, MultipleLongWritable>> getEdges(String[] tokens)
                throws IOException {
            List<Edge<LongWritable, MultipleLongWritable>> edges =
                    Lists.newArrayListWithCapacity(0);
            return edges;
        }
    }
}
